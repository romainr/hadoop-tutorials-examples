package rkanter;

public class MyELFunctions {
    /**
     * Compares two strings while ignoring case.
     *
     * @param s1 first string.
     * @param s2 second string.
     * @return true if <code>s1</code> and <code>s2</code> are equal, regardless of case, and false otherwise
     */
    public static boolean equalsIgnoreCase(String s1, String s2) {
        if (s1 == null) {
            return (s2 == null);
        }
        return s1.equalsIgnoreCase(s2);
    }
}