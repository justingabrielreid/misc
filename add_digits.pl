#!/usr/bin/env perl

use strict;

print "Please enter an integer with two or more digits: ";
chomp(my $n = <STDIN>);
unless ($n =~ /^\d{2,}$/) {
    die "Bad input.\n";
}

print $n, " reduces to ", add_digits($n), "\n";

sub add_digits {
    my $n = shift;
    if (length($n) == 1) {
        return $n;
    }
    else {
        my $sum = 0;
        for my $i (split(//, $n)) {
            $sum += $i;
        }
        add_digits($sum);
    }
}
