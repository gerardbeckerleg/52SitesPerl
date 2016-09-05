use strict;
use warnings;
use ExtUtils::MakeMaker;

WriteMakefile(
    NAME                => 'My::Module',
    AUTHOR              => 'Gerard <gerardbeckerleg@outlook.com>',
    VERSION_FROM        => 'lib/My/Module.pm',
    ABSTRACT_FROM       => 'lib/My/Module.pm',
    PL_FILES            => {},
    PREREQ_PM => {
        'Test::More' => 0,
        'version'    => 0,
    },
    dist                => { COMPRESS => 'gzip -9f', SUFFIX => 'gz', },
    clean               => { FILES => 'My-Module-*' },
);
