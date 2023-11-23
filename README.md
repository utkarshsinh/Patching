# Patching
## Implemented Control Flow Integrity for Secure Software Execution
In a key project, I engineered a robust Control Flow Integrity (CFI) system to enhance software security. This involved disassembling a binary using Datalog Disassembler (ddisasm) and then systematically injecting CFI checks within the assembly code. I strategically inserted prefetchnta instructions after each callq to mark valid return points and modified retq instructions to redirect to a custom validation function, ensuring returns were only made to authenticated points in the code. This process effectively mitigated a known buffer overflow vulnerability, as evidenced by the absence of crashes with previously failing inputs. The project required meticulous coding in assembly, proficiency with debugging tools like GDB, and a deep understanding of software vulnerabilities and exploits. Successful recompilation and testing of the binary demonstrated the efficacy of the CFI implementation in enhancing the application's security without compromising its functionality.
## Technical Skills
*Languages: Python, Assembly, Bash Scripting
*Tools: AFL++, Radamsa, Datalog Disassembler, Docker, GCC, GDB
Concepts: Binary Disassembly, Control Flow Integrity (CFI), Software Hardening, Dockerization, Fuzz Testing, Vulnerability Identification and Mitigation
## Skill Set
Binary Hardening: Automated patching techniques for CGC binaries to enhance security.
Binary Security: Integration of Control Flow Integrity (CFI) for robust defense against exploits.
Automation: Scripted solutions for patching processes, minimizing the need for manual intervention.
Binary Specialization: Proficiency with statically linked libraries and x64 instruction set.
## Tools:
Datalog Disassembler: For disassembling and analyzing binary executables.
Docker: Containerization for consistent and isolated testing environments.
GCC: Utilization of the GNU Compiler Collection for code compilation and linking.
Bash: Scripting for process automation and task execution.
