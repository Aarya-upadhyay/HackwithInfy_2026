class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        line_words = []
        line_len = 0

        for word in words:
            # check if word fits in current line
            if line_len + len(word) + len(line_words) <= maxWidth:
                line_words.append(word)
                line_len += len(word)
            else:
                # justify current line
                res.append(self.justify(line_words, line_len, maxWidth))
                # reset for next line
                line_words = [word]
                line_len = len(word)

        # last line (left justified)
        last_line = " ".join(line_words)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res

    def justify(self, line_words, line_len, maxWidth):
        # if only one word → left justify
        if len(line_words) == 1:
            return line_words[0] + " " * (maxWidth - len(line_words[0]))

        total_spaces = maxWidth - line_len
        gaps = len(line_words) - 1

        space_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        res = ""

        for i in range(len(line_words)):
            res += line_words[i]

            if i < gaps:
                spaces = space_per_gap
                if i < extra_spaces:
                    spaces += 1
                res += " " * spaces

        return res
