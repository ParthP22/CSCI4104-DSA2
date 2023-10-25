public class Main {
    public static void main(String[] args){
        //I did this for DSA II, Problem Set 3, because
        //ain't way am I going to do 216 calculations for this
        //algorithm by hand lol.
        //So I decided to just write this program real quick like 20 minutes
        //before the assignment was due and copied down each
        //iteration of the outer loop.

        int infinity = Integer.MAX_VALUE;
        long[][] W = {{0,infinity,infinity,infinity,-1,infinity},
                {1,0,infinity,2,infinity,infinity},
                {infinity,2,0,infinity,infinity,-8},
                {-4,infinity,infinity,0,3,infinity},
                {infinity,7,infinity,infinity,0,infinity},
                {infinity,5,10,infinity,infinity,0}};

        long[][] D = {{0,infinity,infinity,infinity,-1,infinity},
                {1,0,infinity,2,infinity,infinity},
                {infinity,2,0,infinity,infinity,-8},
                {-4,infinity,infinity,0,3,infinity},
                {infinity,7,infinity,infinity,0,infinity},
                {infinity,5,10,infinity,infinity,0}};

        System.out.println("0: ");
        printMatrix(D);
        for(int k = 0; k < D.length; k++){
            for(int i = 0; i < D.length; i++){
                for(int j = 0; j < D.length; j++){
                    D[i][j] = Math.min(D[i][j], D[i][k] + D[k][j]);
                }
            }
            System.out.println((k + 1) + ": ");
            printMatrix(D);
        }

    }

    public static void printMatrix(long[][] D){
        for(int i = 0; i < D.length; i++){
            for(int j = 0; j < D.length; j++){
                System.out.print(D[i][j] + ",  ");
            }
            System.out.println();
        }
        System.out.println("\n\n");
    }

}
