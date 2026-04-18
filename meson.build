project(
  'lmdbxx',
  'cpp',
  version : '1.0.1',
  license: 'Unlicense',
  default_options : ['warning_level=3', 'cpp_std=c++17']
)

lmdb_dep = dependency('lmdb')

lmdbxx_dep = declare_dependency(
  include_directories : 'include/',
  dependencies: lmdb_dep
)
meson.override_dependency('lmdb++', lmdbxx_dep)

install_headers('lmdb++.h', subdir: 'lmdbxx')

pkg = import('pkgconfig')
pkg.generate(
  libraries: [lmdbxx_dep, lmdb_dep],
  name: 'lmdbxx',
  description: 'C++17 wrapper for the LMDB embedded B+ tree database library',
  install_dir: join_paths(get_option('datadir'), 'pkgconfig')
)

if get_option('examples')
  executable(
    'example',
    'example.cc',
    dependencies: lmdbxx_dep,
    install: false
  )
endif

if get_option('tests')
  check = executable(
    'check',
    'check.cc',
    dependencies: lmdbxx_dep,
    install: false
  )

  test('check', check)
endif

# -----------------------------
# Uninstall support (generated)
# -----------------------------

logfile = join_paths(meson.current_build_dir(), 'meson-logs/install-log.txt')

configure_file(
  output: 'uninstall.sh',
  input: files(),  # inline content below
  command: [
    'sh', '-c',
    '''
cat > @OUTPUT@ << "EOF"
#!/bin/sh
set -e

LOGFILE="''' + logfile + '''"

if [ ! -f "$LOGFILE" ]; then
  echo "Install log not found: $LOGFILE"
  exit 1
fi

echo "Uninstalling files listed in $LOGFILE"

if command -v tac >/dev/null 2>&1; then
  tac "$LOGFILE"
else
  tail -r "$LOGFILE"
fi | while read -r file; do
  if [ -e "$file" ]; then
    echo "Removing $file"
    rm -v "$file"
  fi
done
EOF
'''
  ],
  install: false
)

uninstall_prog = find_program(join_paths(meson.current_build_dir(), 'uninstall.sh'))

custom_target(
  'remove',
  output: 'uninstall.stamp',   # ✅ required dummy output
  command: [uninstall_prog],
  build_by_default: false
)
