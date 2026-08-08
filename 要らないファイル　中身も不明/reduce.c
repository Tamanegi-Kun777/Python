#include <stdio.h>

void main(void) {
    int price;
    printf("通常価格は");
    scanf("%d", &price);
    printf("通常価格は%d円", price);
    /*printf("1割引は %d 円,3割引は %d 円,5割引は %d 円,8割引は %d 円\n", (int)(normal_price * 0.9), (int)(normal_price * 0.7), (int)(normal_price * 0.5), (int)(normal_price * 0.2));*/
}