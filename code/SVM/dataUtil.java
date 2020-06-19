import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;


public class dataUtil {
    public static float[][] readerData(String filename){
        int len = 0;
		
		//read input file to get total rows in input file
        try{
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            reader.readLine();
            String line = null;
            while((line = reader.readLine()) != null){
                len++;
            }
        }catch (Exception e){
            e.printStackTrace();
        }

        float input[][] = new float[len][7];
        int i = 0;
		
		//read input data and save in an array
        try{
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            reader.readLine();
            String line = null;
            while((line = reader.readLine()) != null){
                String item[] = line.split(",");
                //String res = input[input.length - 1];
                //System.out.println(res);
                input[i][0] = Integer.parseInt(item[0]); //sex
                input[i][1] = Integer.parseInt(item[1]); //age
                input[i][2] = Integer.parseInt(item[2]); //country
                input[i][3] = Integer.parseInt(item[3]); //province
                input[i][4] = Integer.parseInt(item[4]); //infection_case
                input[i][5] = Integer.parseInt(item[5]); //infection_order
                input[i][6] = Integer.parseInt(item[6]); //state
                i++;
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        return input;
    }

    /*
    normalize data
     */
    public static void normalize(float[][] input){
        int len = input.length;
        for(int i = 0; i < len; ++i){
            input[i][1] = input[i][1] / 11; //age
            input[i][2] = input[i][1] / 11; //country
            input[i][3] = input[i][1] / 16; //province
            input[i][4] = input[i][1] / 23; //infection_case
            input[i][5] = input[i][1] / 6; //infection_order
            input[i][6] = input[i][1] / 2; //state
        }
    }

    /*
    create train and test set with input ratio
     */
    public static Map<String, float[][]> createTrain(float[][] input, double ratio){
        Map<Integer, float[]> map = new HashMap<>();
        Map<String, float[][]> res = new HashMap<>();
        int len = input.length;
        for(int i = 0; i < len; ++i){
            map.put(i, input[i]);
        }

        int testRows = len - (int)(len * ratio);
        Set<Integer> setTest = randomSet(0, len, testRows, new HashSet<Integer>());
        float[][] testInput = new float[setTest.size()][6];
        float[][] trainInput = new float[len - setTest.size()][6];
        int countTest = 0;
        for(int i : setTest){
            testInput[countTest] = map.get(i);
            map.remove(i);
            countTest++;
        }
        res.put("test", testInput);

        int countTrain = 0;
        for(int i : map.keySet()){
            trainInput[countTrain] = map.get(i);
            //map.remove(i);
            countTrain++;
        }
        res.put("train", trainInput);
        return res;
    }

    /*
    create random set which will be used in picking random data to create train and test set
     */
    public static Set<Integer> randomSet(int min, int max, int n, HashSet<Integer> set) {
        if (n > (max - min + 1) || max < min) {
            return set;
        }
        for (int i = 0; i < n; i++) {
            // create random number
            int num = (int) (Math.random() * (max - min)) + min;
            set.add(num);// add random number into HashSet to make sure every number is unique
        }
        int setSize = set.size();
        // recursively create random number till the condition
        if (setSize < n) {
            randomSet(min, max, n - setSize, set);
        }
        return set;
    }

    /*
    extract state feature as the data's label
     */
    public static Map<String, float[][]> extractLabel(float[][] input){
        Map<String, float[][]> res = new HashMap<>();
        int len = input.length;
        int col = input[0].length;
        float[][] data = new float[len][col - 1];
        float[][] label = new float[len][1];
        for(int i = 0; i < len; ++i){
            label[i][0] = input[i][col - 1];
            for(int j = 0; j < col - 1; ++j){
                data[i][j] = input[i][j];
            }
        }
        res.put("data",data);
        res.put("label",label);
        return res;
    }

    /*
    remove some state which to create a  two classifier
     */
    public static float[][] removeState(float[][] input, int state){
        int len = input.length;
        int col = input[0].length;
        int j = 0;
        for(int i = 0; i < len; ++i){
            if(input[i][col - 1] == state){
                j = j + 1;
            }
        }
        float[][] res = new float[len - j][col];
        j = 0;
        for(int i = 0; i< len; ++i){
            if(input[i][col - 1] != state){
                res[j] = input[i];
                j = j + 1;
            }
        }
        return res;
    }
}
