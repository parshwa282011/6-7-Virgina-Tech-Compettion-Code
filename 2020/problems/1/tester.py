#!/usr/bin/env python3
"""
tester.py
Run a target Python script (default ./1.py) with stdin taken from an input file
and print the inputs (echo) and the target's outputs.

Usage:
  python3 tester.py [input-file] [target-script]

Defaults:
  input-file: input.txt (in the same folder)
  target-script: ./1.py
"""
import sys
import subprocess
import os


def main():
    inp_file = sys.argv[1] if len(sys.argv) > 1 else './input.txt'
    target = sys.argv[2] if len(sys.argv) > 2 else './1.py'
    out_file = sys.argv[3] if len(sys.argv) > 3 else './output.txt'

    if not os.path.exists(inp_file):
        print(f"Input file not found: {inp_file}", file=sys.stderr)
        sys.exit(2)
    if not os.path.exists(target):
        print(f"Target script not found: {target}", file=sys.stderr)
        sys.exit(3)

    with open(inp_file, 'r') as f:
        lines = f.readlines()

    num_testcases = int(lines[0].strip())
    
    with open(out_file, 'w') as out:
        out.write(f"Number of test cases: {num_testcases}\n\n")

        line_idx = 1
        for tc_num in range(1, num_testcases + 1):
            out.write(f"=== TEST CASE {tc_num} ===\n")
            
            # Determine the extent of this test case
            tc_start = line_idx
            if line_idx < len(lines):
                first_val = int(lines[line_idx].strip())
                tc_end = line_idx + 1 + first_val
            else:
                tc_end = len(lines)

            # Extract this test case's input
            tc_input_lines = lines[tc_start:tc_end]
            tc_input = ''.join(tc_input_lines)

            out.write("--- INPUT ---\n")
            out.write(tc_input)
            out.write("--- END INPUT ---\n")

            # Run the target with this test case's input
            proc = subprocess.run(
                [sys.executable, target],
                input=tc_input.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            out.write("--- OUTPUT (stdout) ---\n")
            out.write(proc.stdout.decode(errors='replace'))

            if proc.stderr:
                out.write("--- OUTPUT (stderr) ---\n")
                out.write(proc.stderr.decode(errors='replace'))

            out.write(f"--- RETURN CODE: {proc.returncode} ---\n\n")

            line_idx = tc_end
    
    print(f"Test results written to {out_file}")


if __name__ == '__main__':
    main()