#!/usr/bin/env perl

use strict;
use warnings;

my $gh_url = "https://GITHUB_REPO";
my $target_dir = "FOLDER_TO_KEEP_UPDATED";

my $temp_repo_location = "/tmp/temp_repo_location";

# clone gh repo to temp dir
system("rm", "-rf", "$temp_repo_location");
system("git", "clone", "$gh_url", "$temp_repo_location");

# don't compare .git files
system("rm", "-rf", "$temp_repo_location/.git");

# compare differences
system("diff", "-r", "$target_dir", "$temp_repo_location");

if ($?) {
  system("rm", "-rf", "$target_dir");
  system("cp", "-r", "$temp_repo_location", "$target_dir");
  print "Detected a difference!\n";
}

exit 0;
