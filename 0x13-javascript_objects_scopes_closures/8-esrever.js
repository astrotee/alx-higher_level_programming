#!/usr/bin/node

exports.esrever = function (list) {
  const rl = [];
  for (const el of list) {
    rl.unshift(el);
  }
  return rl;
};
