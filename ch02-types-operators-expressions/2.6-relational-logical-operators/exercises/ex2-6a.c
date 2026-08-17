unsigned setbits(unsigned x, int p, int n, unsigned y)
{
    unsigned mask = ~(~0 << n);

    x &= ~(mask << (p + 1 - n));

    x |= (y & mask) << (p + 1 - n);

    return x;
}
