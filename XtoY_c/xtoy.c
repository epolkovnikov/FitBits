#include "xtoy.h"
#include <assert.h>
#include <string.h>

/* Convert given integer of radix 10 to a given radix and output as string.
   i - integer of base 10 to convert
   a - result string pointer
   radix - target base
*/
void my_itoa(int i, char* a, int radix)
{
    int ii = i; /* i internal*/
    int j = 0;  /* string counter */
    int jf = 0, jr = 0;  /* reverse string counters */
    char ct = '0';
    char num[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    assert(a);
    
    /* switch the sign to avoid wrong charcodes */ 
    if (0 > i)
    {
       ii *= -1;
    }
       
    /* Extract digits to string */
    do
    {
       a[j] = num[ii % radix];
       j++;
       ii /= radix; /* this will give 0 at the end */
    } while (0 != ii);

    /* put the sign */
    if (0 > i)
    {
       a[j] = '-';
       j++;
    }
       
    /* Reverse the result string */
    for (jf = 0, jr = j-1 ; jf < jr; jf++, jr--)
    {
       ct    = a[jr];
       a[jr] = a[jf];
       a[jf] = ct;
    }
    a[j] = 0;
};
/* The same as my_itoa but with pointer arithmetic. */
void my_itoa_pa(int i, char* a, int radix)
{
    int ii = i; /* i internal*/
    char ct = '0';
    char* s = (char*)a;
    char* e;
    char num[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    assert(a);

    /* switch the sign to avoid wrong charcodes */ 
    if (0 > i)
    {
       ii *= -1;
    }
       
    /* Extract digits to string */
    do
    {
       *a++ = num[ii % radix];
    } while (0 != (ii /= radix));

    /* put the sign */
    if (0 > i)
    {
       *a++ = '-';
    }
       
    /* Reverse the result string */
    e = a - 1;
    while (e > s)
    {
       ct   = *a;
       *a-- = *s;
       *s++ = ct;
    }
    a = 0;
};
/* atoi assuming radix 10 */
int my_atoi(const char* a)
{
    int   res_i = 0;
    int   pow_10 = 1;
    char* p_c;

    assert(a);

    /* get the last item */
    p_c = (char*)(a + strlen(a) - 1);

    /* Check string items one by one and if they are numerical - add them to the number */
    do 
    {
        /* Identify if we have a number */
        if (('0' <= *p_c) && ('9' >= *p_c))
        {
            res_i += (int)(*p_c - '0') * pow_10;
            pow_10 *= 10;
        }
    }
    while (a != p_c--); /* It is potentially risky pointer here */
    
    /* Determine the sign */
    if ('-' == *a) res_i = -res_i;
       
    return res_i;
};
