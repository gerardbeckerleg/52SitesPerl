use Test::More tests => 1;

BEGIN {
use_ok( 'My::Module' );
}

diag( "Testing My::Module $My::Module::VERSION" );
