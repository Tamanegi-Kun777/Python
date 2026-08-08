#include <ctype.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "9cc.h"

// 入力プログラム(実体はここに1つだけ置く)
char *user_input;

// 現在着目しているトークン(実体はここに1つだけ置く)
Token *token;

void error(char *fmt, ...) {
  va_list ap;
  va_start(ap, fmt);
  vfprintf(stderr, fmt, ap);
  fprintf(stderr, "\n");
  exit(1);
}
 
void error_at(char *loc, char *fmt, ...) {
  va_list ap;
  va_start(ap, fmt);
 
  int pos = loc - user_input;
  fprintf(stderr, "%s\n", user_input);
  fprintf(stderr, "%*s", pos, " "); // pos個の空白を出力
  fprintf(stderr, "^ ");
  vfprintf(stderr, fmt, ap);
  fprintf(stderr, "\n");
  exit(1);
}

bool startswith(char *p, char *q) {
  return memcmp(p, q, strlen(q)) == 0;
}

// 新しいトークンを作成してcurに繋げる
Token *new_token(TokenKind kind, Token *cur, char *str, int len) {
  Token *tok = calloc(1, sizeof(Token));
  tok->kind = kind;
  tok->str = str;
  tok->len = len;
  cur->next = tok;
  return tok;
}

// 入力文字列pをトークナイズしてそれを返す
Token *tokenize() {
  char *p = user_input;
  Token head;
  head.next = NULL;
  Token *cur = &head;
 
  while (*p) {
    // 空白文字をスキップ
    if (isspace(*p)) {
      p++;
      continue;
    }
    if ('a' <= *p && *p <= 'z') {
      cur = new_token(TK_IDENT, cur, p, 1);
      p++;
      cur->len = 1;
      continue;
}
    // ===== ここから追加: 記号のトークナイズが無かったため追加 =====

    // ===== 追加ここまで =====
    // Multi-letter punctuator
    if (startswith(p, "==") || startswith(p, "!=") ||
        startswith(p, "<=") || startswith(p, ">=")) {
      cur = new_token(TK_RESERVED, cur, p, 2);
      p += 2;
      continue;
    }

    // Single-letter punctuator
    if (strchr("+-*/()<>=;", *p)) {
      cur = new_token(TK_RESERVED, cur, p++, 1);
      continue;
    }
    // Integer literal
    if (isdigit(*p)) {
      cur = new_token(TK_NUM, cur, p, 0);
      char *q = p;
      cur->val = strtol(p, &p, 10);
      cur->len = p - q;
      continue;
    }
    error_at(p, "invalid token"); 
  }
  new_token(TK_EOF, cur, p, 0);
  return head.next;
}
