class Solution {
    public String reversePrefix(String word, char ch) {
        
        char[] str = word.toCharArray();
        int pos = -1;

        for (int i=0; i<str.length; i++) {
            if (str[i] == ch) {
                pos = i;
                break;
            }
        }

        if (pos == -1) return word;

        StringBuilder builder = new StringBuilder();
        for (int i=pos ; i>=0; i--) {
            builder.append(str[i]);
        }

        if (pos+1 < str.length) {
            for (int i=pos+1 ; i<str.length; i++) {
                builder.append(str[i]);
            }
        }

        return builder.toString();
    }
}