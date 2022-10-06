#include <stdio.h>
#include <string.h>
#include "xtoy.h"

const struct
{
    char* failed;
    char* passed; 
} test_result = {"FAIL", "pass"};

typedef struct {
    int   value; /* value to test */
    int   radix; /* radix to convert value */
    char* ret;  /* expected return value */
    char* tag;  /* comment text */
} ITOA_UT_DATA_S_T;

typedef struct {
    int   ret;   /* expected return value */
    char* value; /* value to test */
    char* tag;   /* comment text */
} ATOI_UT_DATA_S_T;

const ITOA_UT_DATA_S_T itoa_ut[] =
{
    {     0, 2,      "0", "itoa Zero value (0)"},
    {     1, 2,      "1", "itoa value (1)"},
    {    10, 10,     "10", "itoa radix value (10)"},
    { 32767, 2,  "111111111111111", "itoa Max value (32767)"},
    {-32768, 10, "-32768", "itoa Max value (-32768)"},
    {    10, 16,      "A", "itoa (10=0xA)"},
    {    10,  2,   "1010", "itoa (10=bx1010)"},
    { 32767,  62,   "8WV"  , "itoa (32767=8WV)"},
};
const unsigned int itoa_ut_max = sizeof(itoa_ut)/sizeof(itoa_ut[0]);

const ITOA_UT_DATA_S_T itoa_pa_ut[] =
{
    {     0, 10,      "0", "itoa_pa Zero value (0)"},
    {     1, 10,      "1", "itoa_pa value (1)"},
    {    10, 10,     "10", "itoa_pa radix value (10)"},
    { 32767, 10,  "32767", "itoa_pa Max value (32767)"},
    {-32768, 10, "-32768", "itoa_pa Max value (-32768)"},
    {    10, 16,      "A", "itoa_pa (10=0xA)"},
    {    10,  2,   "1010", "itoa_pa (10=bx1010)"}
};
const unsigned int itoa_pa_ut_max = sizeof(itoa_pa_ut)/sizeof(itoa_pa_ut[0]);

const ATOI_UT_DATA_S_T atoi_ut[] =
{
    {     0,      "0", "atoi Zero value (0)"},
    {     1,      "1", "atoi value (1)"},
    {    10,     "10", "atoi radix value (10)"},
    { 32767,  "32767", "atoi Max value (32767)"},
    {-32768, "-32768", "atoi Min value (-32768)"}
};
const unsigned int atoi_ut_max = sizeof(atoi_ut)/sizeof(atoi_ut[0]);

int main(int argc, char *argv[])
{
    char itoa_ut_a[35] = {0};
    int i;
    char* tresult = test_result.passed;
    unsigned int tfc = 0; /* tests failure counter */

    /* itoa Unit Test */   
    printf("----- my_itoa start ------\n");
    for (i = 0; i < itoa_ut_max; i++)
    {
        my_itoa(itoa_ut[i].value, &itoa_ut_a[0], itoa_ut[i].radix);
        if (0 == strcmp(&itoa_ut_a[0], itoa_ut[i].ret))
        {
            tresult = test_result.passed;
        }
        else
        {
            tresult = test_result.failed;
            tfc++;
        }
        printf("%s: radix==%d %s\t= %s\n", tresult, itoa_ut[i].radix, itoa_ut[i].tag, &itoa_ut_a[0]);
    }
    if (0 != tfc) tresult = test_result.failed;
    printf("result itoa = %s\n", tresult);
    printf("----- my_itoa end ------\n");

    /* itoa_pa Unit Test */   
    printf("----- my_itoa_pa start ------\n");
    tfc = 0;
    for (i = 0; i < itoa_pa_ut_max; i++)
    {
        my_itoa(itoa_pa_ut[i].value, &itoa_ut_a[0], itoa_pa_ut[i].radix);
        if (0 == strcmp(&itoa_ut_a[0], itoa_pa_ut[i].ret))
        {
            tresult = test_result.passed;
        }
        else
        {
            tresult = test_result.failed;
            tfc++;
        }
        printf("%s: radix==%d %s\t= %s\n", tresult, itoa_pa_ut[i].radix, itoa_pa_ut[i].tag, &itoa_ut_a[0]);
    }
    if (0 != tfc) tresult = test_result.failed;
    printf("result my_itoa_pa = %s\n", tresult);
    printf("----- my_itoa_pa end ------\n");

    printf("----- my_atoi start ------\n");
    tfc = 0;
    for (i = 0; i < atoi_ut_max; i++)
    {
        if (atoi_ut[i].ret == my_atoi(atoi_ut[i].value))
        {
            tresult = test_result.passed;
        }
        else
        {
            tresult = test_result.failed;
            tfc++;
        }
        printf("%s: %s %s\t= %d\n", tresult, atoi_ut[i].tag, atoi_ut[i].value, my_atoi(atoi_ut[i].value));
    }
    if (0 != tfc) tresult = test_result.failed;
    printf("result my_atoi = %s\n", tresult);
    printf("----- my_atoi end ------\n");


    return 0;
};
