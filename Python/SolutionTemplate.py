from typing import List

class Solution:
    def temp(self): 
        pass


if __name__ == "__main__":
    solutionClass = Solution()
    solution = getattr(solutionClass,[func for func in dir(solutionClass) if not func.startswith("__")][0])
    testcases = [
        ({},0)
    ]
    print("-----")
    for testcase in testcases:
        output = solution(**testcase[0])
        print("✅ PASSED" if  testcase[1] == output else "❌ FAILED", 
                              f"Input\n- {testcase[0]}", 
                              f"Output\n- {output}",
                              f"Expected\n- {testcase[1]}",
                              "-----", sep="\n")
