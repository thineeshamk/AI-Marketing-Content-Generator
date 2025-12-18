import os

def run_test(script_name):
    print(f"\n🔹 Running {script_name}...")
    exit_code = os.system(f"python tests/{script_name}")
    if exit_code == 0:
        print(f"✅ {script_name} PASSED")
    else:
        print(f"❌ {script_name} FAILED")

if __name__ == "__main__":
    print("🚀 Starting Marketing Agent QA Suite...")
    run_test("test_trends.py")
    run_test("test_brain.py")
    run_test("test_full_flow.py")
    print("\n🏁 QA Complete.")
