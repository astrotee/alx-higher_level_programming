#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = n; i > 0; i--) {
    console.log('X'.repeat(n));
  }
}
