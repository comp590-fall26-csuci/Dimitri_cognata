#include "utest.h"
#include "fibonacci.h"

UTEST(fibonacci, terms_1_to_10) {
    int expected[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    for (int i = 1; i <= 10; i++) {
        ASSERT_EQ(expected[i - 1], fibonacci(i));
    }
}

UTEST_MAIN();
