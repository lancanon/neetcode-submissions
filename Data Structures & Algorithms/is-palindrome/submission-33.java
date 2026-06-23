class Solution {
    public boolean isPalindrome(String s) {

        // Start one pointer at the beginning
        int left = 0;

        // Start one pointer at the end
        int right = s.length() - 1;

        // Keep checking until pointers meet in the middle
        while (left < right) {

            // Move left pointer forward while current character
            // is NOT a letter or number
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // Move right pointer backward while current character
            // is NOT a letter or number
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // Convert both characters to lowercase so that
            // 'A' and 'a' are treated as the same character
            char leftChar = Character.toLowerCase(s.charAt(left));
            char rightChar = Character.toLowerCase(s.charAt(right));

            // If the characters don't match,
            // it cannot be a palindrome
            if (leftChar != rightChar) {
                return false;
            }

            // Move both pointers toward the center
            left++;
            right--;
        }

        // If we checked everything without finding a mismatch,
        // the string is a palindrome
        return true;
    }
}