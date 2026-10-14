#!/usr/bin/env python3
"""run_tests.py — regression tests for scripts/check_article.py.

One fixture per rule ID (fail/) or clean sample (pass/). Run from anywhere:
    python tests/run_tests.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "scripts" / "check_article.py"
FIX = ROOT / "tests" / "fixtures"

def run(path, hook=False):
    cmd = [sys.executable, str(CHECKER), str(path)] + (["--hook"] if hook else [])
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout

# (label, path, hook, expected_exit, must_contain, must_not_contain)
CASES = [
    ("sample-article passes with --hook", ROOT/"examples/sample-article.md", True, 0, ["0 error(s), 0 warning(s)"], []),
    ("pass_minimal clean", FIX/"pass/pass_minimal.md", False, 0, ["0 error"], []),
    ("R1 banned phrases", FIX/"fail/R1_banned.md", False, 1, ['"综上所述"', '"It\'s worth noting"', '"总的来说"'], []),
    ("G7 paragraph >5 sentences", FIX/"fail/G7_long_para.md", False, 1, ["paragraph has 6 sentences"], []),
    ("G8 hook too short", FIX/"fail/G8_hook_short.md", True, 1, ["opening hook"], []),
    ("G8 hook too long", FIX/"fail/G8_hook_long.md", True, 1, ["opening hook"], []),
    ("guard: 本文 once, 本文件 never", FIX/"fail/guard_benwen.md", False, 0, ['"本文"'], ["本文件"]),
    ("check:off exemption", FIX/"fail/checkoff_exempt.md", False, 0, ["0 error"], []),
    ("R1 enumeration >=3", FIX/"fail/R1_enum.md", False, 1, ["enumeration"], []),
    ("combo multi-violation", FIX/"fail/combo.md", False, 1, ['"综上所述"', "enumeration"], []),
]

def main():
    failed = 0
    for label, path, hook, code, must, mustnot in CASES:
        rc, out = run(path, hook)
        ok = (rc == code) and all(m in out for m in must) and all(m not in out for m in mustnot)
        print(f"{'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failed += 1
            print(f"      exit={rc} (want {code})")
            for m in must:
                if m not in out: print(f"      missing: {m}")
            for m in mustnot:
                if m in out: print(f"      should-not-contain: {m}")
            print("      --- output ---")
            print("      " + "\n      ".join(out.splitlines()[:8]))
    print(f"\n{len(CASES)-failed}/{len(CASES)} passed")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
