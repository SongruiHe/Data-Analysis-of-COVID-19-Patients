import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class numerical {
    public static void main(String[] args) {
        String filename = "D:\\[CS235]\\dataset\\PatientInfo-csv.csv"; //input file's name
        int len = 0;
		//read input file to get total rows input file
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

        String input[][] = new String[len][7];
        int i = 0;
		
		//select 7 features in input file and save in an array
        try{
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            reader.readLine();
            String line = null;
            while((line = reader.readLine()) != null){
                String item[] = line.split(",");
                //String res = input[input.length - 1];
                //System.out.println(res);
                input[i][0] = item[1]; //sex
                input[i][1] = item[3]; //age
                input[i][2] = item[4]; //country
                input[i][3] = item[5]; //province
                input[i][4] = item[8]; //infection_case
                input[i][5] = item[9]; //infection_order
                input[i][6] = item[16]; //state
                i++;
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        //System.out.println(input.length);
		
		//create hashmap to record different values in each feature and set every type of value an id (numerical input files from string to integer)
        HashMap<String, Integer> mapSex = new HashMap<>();
        HashMap<String, Integer> mapAge = new HashMap<>();
        HashMap<String, Integer> mapCountry = new HashMap<>();
        HashMap<String, Integer> mapProvince = new HashMap<>();
        HashMap<String, Integer> mapInfectionCase = new HashMap<>();
        HashMap<String, Integer> mapInfectionOrder = new HashMap<>();
        HashMap<String, Integer> mapState = new HashMap<>();
        int countSex = 0, countAge = 0, countCountry = 0, countProvince = 0,
                countIC = 0, countIO = 0, countState = 0;
        for(int j = 0; j < len; j++){
            for(int k = 0; k < input[0].length; k++){
                if(input[j][k] == null)
                    input[j][k] = "unknown";
            }
            if(!mapSex.containsKey(input[j][0])){
                mapSex.put(input[j][0], countSex++);
            }
            if(!mapAge.containsKey(input[j][1])){
                mapAge.put(input[j][1], countAge++);
            }
            if(!mapCountry.containsKey(input[j][2])){
                mapCountry.put(input[j][2], countCountry++);
            }
            if(!mapProvince.containsKey(input[j][3])){
                mapProvince.put(input[j][3], countProvince++);
            }
            if(!mapInfectionCase.containsKey(input[j][4])){
                mapInfectionCase.put(input[j][4], countIC++);
            }
            if(!mapInfectionOrder.containsKey(input[j][5])){
                mapInfectionOrder.put(input[j][5], countIO++);
            }
            if(!mapState.containsKey(input[j][6])){
                mapState.put(input[j][6], countState++);
            }
        }

		//write out the numerical data
        try {
            File csv = new File("D:\\[CS235]\\numerical.csv");
            BufferedWriter bw = new BufferedWriter(new FileWriter(csv, true));
            bw.write("sex"+","+"age"+","+"country"+","+"province"+","+"infection_case"+","+"infection_order"+","+"state");
            bw.newLine();
            for(int j = 0; j < len; j++){
                bw.write(mapSex.get(input[j][0])+","+mapAge.get(input[j][1])+","+
                        mapCountry.get(input[j][2])+","+mapProvince.get(input[j][3])+","+
                        mapInfectionCase.get(input[j][4])+","+mapInfectionOrder.get(input[j][5])+","+
                        mapState.get(input[j][6])+",");
                bw.newLine();
            }
            bw.close();
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
