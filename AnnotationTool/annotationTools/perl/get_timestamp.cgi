#!/usr/bin/perl
use FindBin;
use File::Spec;
use lib File::Spec->catdir($FindBin::Bin);
require 'globalvariables.pl';
require 'logfile_helper.pl';


# Get the timestamp:
$datestr = &GetTimeStamp;

print "Content-type: text/html\n\n";
print "$datestr";
