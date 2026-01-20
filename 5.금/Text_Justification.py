class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        n = len(words)
        idx = 0

        while idx < n:
            current_line_words = []
            current_line_length = 0 
            
            line_start_idx = idx 
            while idx < n and current_line_length + len(words[idx]) + (len(current_line_words)) <= maxWidth:
                current_line_words.append(words[idx])
                current_line_length += len(words[idx])
                idx += 1
            
            num_words_in_line = len(current_line_words)

            if idx == n or num_words_in_line == 1:
                line = " ".join(current_line_words)
                line += " " * (maxWidth - len(line)) 
                result.append(line)

            else:
                total_spaces_needed = maxWidth - current_line_length
                num_gaps = num_words_in_line - 1 
                
                base_spaces_per_gap = total_spaces_needed // num_gaps
                extra_spaces_for_left_gaps = total_spaces_needed % num_gaps
                
                line = ""
                for i in range(num_words_in_line):
                    line += current_line_words[i]
                    if i < num_gaps: 
                        num_spaces_to_add = base_spaces_per_gap
                        if i < extra_spaces_for_left_gaps:
                            num_spaces_to_add += 1
                        line += " " * num_spaces_to_add
                result.append(line)
                
        return result
