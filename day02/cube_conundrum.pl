#!/usr/bin/env perl
use v5.38;

sub good_set($cubes) {
    my %MAX_COUNT = (red => 12,
                     green => 13,
                     blue => 14,
                    );

    my @toks = split ', ', $cubes;
    for my $tok (@toks) {
        my ($count, $color) = split ' ', $tok;
        return 0 if $count > $MAX_COUNT{$color};
    }
    return 1;
}

sub good_game($game) {
    my @toks = split '; ', $game;
    for my $cubes (@toks) {
        return 0 unless good_set($cubes);
    }
    return 1;
}

sub min_set_prod($game) {
    my %min_set = map {$_ => 0} qw(red green blue);

    my @game_toks = split '; ', $game;
    for my $cubes (@game_toks) {
        my @cube_toks = split ', ', $cubes;
        for my $tok (@cube_toks) {
            my ($count, $color) = split ' ', $tok;
            $min_set{$color} = $count if $count > $min_set{$color};
        }
    }
    return $min_set{red} * $min_set{green} * $min_set{blue};
}

my $part1 = 0;
my $part2 = 0;
while (<>) {
    chomp;
    if (/Game (\d+): (.*)/) {
        my ($game_num, $game) = ($1, $2);
        $part1 += $game_num if good_game($game);
        $part2 += min_set_prod($game);
    }
}

say "Part 1: $part1";
say "Part 2: $part2";
