class 411-230 {
    public static void main(String[] args) {
        double x0 = 3.0;
        double x1 = 5.0;
        for (int i = 2; i <= 20; i++) {
            double xn = (1 + x1) / x0;
            System.out.println("X: " + (i) + " , " + xn);
            double tmp = x1;
            x1 = xn;
            x0 = tmp;
        }
    }
}
