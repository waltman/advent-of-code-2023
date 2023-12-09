#!/usr/bin/env perl
use v5.38;
use List::Util qw(any sum);

my @reports = map {[split]} <>;

printf "Part 1: %d\n", sum(map {next_val($_)} @reports);
printf "Part 2: %d\n", sum(map {prev_val($_)} @reports);

sub extrapolate($report) {
    my @seqs = ($report);
    push @seqs, [map { $seqs[-1][$_+1] - $seqs[-1][$_] } 0..$seqs[-1]->$#* - 1] while any {$_} $seqs[-1]->@*;
    return \@seqs;
}

sub next_val($report) {
    my $seqs = extrapolate($report);

    my $delta = 0;
    for (my $i = $#$seqs - 1; $i >= 0; $i--) {
	$delta = $seqs->[$i][-1] + $delta;
    }

    return $delta;
}

sub prev_val($report) {
    my $seqs = extrapolate($report);

    my $delta = 0;
    for (my $i = $#$seqs - 1; $i >= 0; $i--) {
	$delta = $seqs->[$i][0] - $delta;
    }

    return $delta;
}

