from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t = p
        left = right = 0
        # [left, right) 是窗口
        # 1- 先不断地增加 right 指针扩大窗口 [left, right);
        #    直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
        # 2- 我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right)
        #    直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了） 每次增加 left，我们都要更新一轮结果
        # 3- 重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头
        # 第 2 步相当于在寻找一个「可行解」，然后第 3 步在优化这个「可行解」，最终找到最优解
        # 左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        window = collections.defaultdict(int)
        # valid 变量表示窗口中满足 need 条件的字符个数，如果 valid 和 need.size 的大小相同
        # 窗口已满足条件，已经完全覆盖了串 T
        valid = 0

        # 记录最小覆盖子串的起始索引及长度
        start = 0
        sub_len = float('inf')
        ret = []
        while right < len(s):
            # 开始滑动 c 是将移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩, 排列长度和s1长度一样
            while right - left >= len(t):
                # 在这里更新最小覆盖子串
                if valid == len(need):
                    ret.append(left)
                # d 是移出窗口的字符
                d = s[left]

                # 窗口缩小
                left += 1

                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 未找到符合条件的子串
        return ret


class Solution:
    def same(self, freq_1, freq_2):
        for i in range(26):
            if freq_1[i] != freq_2[i]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = [0 for i in range(26)]
        freq_s = [0 for i in range(26)]
        res = []
        for c in p:
            freq_p[ord(c) - ord('a')] += 1
        l = 0
        r = -1  # Sliding window: s[l, r]
        while r + 1 < len(s):
            r += 1
            freq_s[ord(s[r]) - ord('a')] += 1;
            if r - l + 1 > len(p):
                freq_s[ord(s[l]) - ord('a')] -= 1
                l += 1

            if r - l + 1 == len(p) and self.same(freq_s, freq_p):
                res.append(l)
        return res
