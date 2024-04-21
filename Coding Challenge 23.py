'''# QUESTION'''
'''
Memory Management
Max Score: 10 | Difficulty: Medium
Description:
Create a function that calculates various components required for address translation in a virtual memory system. Given the parameters of a virtual memory system-such as page size, physical memory size, and the size of the virtual and physical address space-you must determine the number of bits required for the following:
1. Virtual Page Number (VPN)
2. Page Offset
3. Page Table Index
4. Frame Number
5. Offset within a Frame
Input Format
Your function should accept three integers, each in a separate line:
page_size_kb: The size of a page in kilobytes.
physical_memory_kb: The size of the physical memory in kilobytes.
address_space_bits: The size of both the virtual and physical address space in bits.

Output Format
Your function should return a dictionary containing the number of bits required for each of the following components in a separate line:
"VPN" (Virtual Page Number)
"Page Offset"
"Page Table Index"
"Frame Number"
"Offset within a Frame"
Error Handling
Incase any of the input is not a power of 2, show the following message: "Both page size and physical memory size must be powers of two.""
Constraints
page_size_kb and physical_memory_kb will be powers of two. address_space_bits will be a standard value typically found in modern computer systems (e.g., 32 or 64 bits).
Sample input:
4
16
32

Sample output:
"VPN": 20
"Page Offset":12
"Page Table Index": 20
"Frame Number": 2
"Offset within a Frame": 12
Explanation:
Given a page size of 4 KB, physical memory size of 16 KB, and a 32-bit
address space:
Virtual Memory Calculation Details
Context
• Page Size: 4 KB
• Physical Memory Size: 16 KB
• Address Space: 32-bit

Calculation Breakdown
1. Virtual Address Space and Page Size:
• The virtual address space is 32 bits.
• The page size is 4 KB (equivalent to 212 or 4096 bytes), necessitating 12 bits for the page offset.
2. Virtual Page Number (VPN):
• With 12 bits allocated for the page offset, the remaining 20 bits (32-12) are used for the VPN.
• The page table index corresponds directly with the VPN.

3. Physical Memory Frames:
• The physical memory is 16 KB, divided into 4 KB pages/frames.
• This results in 16KB 4KB = 4 frames.
• Thus, 2 bits are needed to represent the frame number.
4. Frame Offset:
• The offset within a frame is identical to the page offset, also 12 bits.
Each component's size aligns with the calculations we performed, and
together they represent the breakdown of a 32-bit virtual address in a demand-paged virtual memory system with the given parameters.
'''


'''4 TEST CASES PASSES'''

import math

def is_power_of_two(x):
    # Returns True if x is a power of two, False otherwise.
    return (x > 0) and (x & (x - 1)) == 0

def calculate_memory_components(page_size_kb, physical_memory_kb, address_space_bits):
    # Calculate the components required for memory management based on inputs.
    if not (is_power_of_two(page_size_kb) and is_power_of_two(physical_memory_kb)):
        return "Both page size and physical memory size must be powers of two."

    # Convert page size from KB to bytes
    page_size_bytes = page_size_kb * 1024
    # Calculate the number of bits needed for the page offset
    page_offset_bits = int(math.log2(page_size_bytes))
    
    # Calculate the number of frames possible in physical memory
    total_frames = physical_memory_kb // page_size_kb
    frame_number_bits = int(math.log2(total_frames))

    # Calculate VPN bits
    vpn_bits = address_space_bits - page_offset_bits
    # Page table index typically matches VPN bits
    page_table_index_bits = vpn_bits
    # Offset within a frame matches page offset bits
    frame_offset_bits = page_offset_bits

    return {
        "VPN": vpn_bits,
        "Page Offset": page_offset_bits,
        "Page Table Index": page_table_index_bits,
        "Frame Number": frame_number_bits,
        "Offset within a Frame": frame_offset_bits
    }


# Input reading section
page_size_kb = int(input())
physical_memory_kb = int(input())
address_space_bits = int(input())

# Calculating memory management components
result = calculate_memory_components(page_size_kb, physical_memory_kb, address_space_bits)

if isinstance(result, str):
    print(result)

else:
    for key, value in result.items():
        print(f'{key}: {value} bits')