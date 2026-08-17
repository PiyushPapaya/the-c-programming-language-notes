unsigned rightrot(unsigned x, int n)
{
    int wordlength = sizeof(unsigned) * 8;

    while (n-- > 0) {
        x = (x >> 1) | (x << (wordlength - 1));
    }

    return x;
}
