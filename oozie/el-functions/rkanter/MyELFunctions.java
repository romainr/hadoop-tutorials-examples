package rkanter;

public class MyELFunctions {
    /**
     * Compares two strings while ignoring case. <p/> A string with <code>null</code> value is considered as an empty
     * string.
     *
     * @param s1 first string.
     * @param s2 second string.
     * @return true if <code>s1</code> and <code>s2</code> are equal, regardless of case, and false otherwise
     */
    public static boolean equalsIgnoreCase(String s1, String s2) {
        if (s1 == null) {
            s1 = "";
        }
        if (s2 == null) {
            s2 = "";
        }
        return s1.equalsIgnoreCase(s2);
    }
}