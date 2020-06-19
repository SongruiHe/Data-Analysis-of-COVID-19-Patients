import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Map;


public class main {
    public static void main(String []arg){
        float[][] input = dataUtil.readerData("D:\\[CS235]\\numerical.csv"); //read data
        Map<String, float[][]> map = dataUtil.createTrain(input, 0.9); //create random train and test set which train:test=9:1
        float[][] trainSet = map.get("train");
        float[][] testSet = map.get("test");
        float[][] trainRI = dataUtil.removeState(trainSet, 2); //remove deceased state
        float[][] trainRD = dataUtil.removeState(trainSet, 1); //remove isolated state
        float[][] trainDI = dataUtil.removeState(trainSet, 0); //remove released state
        //extract corresponding labels
        Map<String, float[][]> mapRI = dataUtil.extractLabel(trainRI);
        Map<String, float[][]> mapRD = dataUtil.extractLabel(trainRD);
        Map<String, float[][]> mapDI = dataUtil.extractLabel(trainDI);
        Map<String, float[][]> map2 = dataUtil.extractLabel(testSet);
        float[][] trainDataRI = mapRI.get("data");
        float[][] trainLRI = mapRI.get("label");
        float[] trainLableRI = new float[trainLRI.length];
        for(int i = 0; i < trainLRI.length; ++i){
            trainLableRI[i] = trainLRI[i][0];
        }
        float[][] trainDataRD = mapRD.get("data");
        float[][] trainLRD = mapRD.get("label");
        float[] trainLableRD = new float[trainLRD.length];
        for(int i = 0; i < trainLRD.length; ++i){
            trainLableRD[i] = trainLRD[i][0];
        }
        float[][] trainDataDI = mapDI.get("data");
        float[][] trainLDI = mapDI.get("label");
        float[] trainLableDI = new float[trainLDI.length];
        for(int i = 0; i < trainLDI.length; ++i){
            trainLableDI[i] = trainLDI[i][0];
        }
        float[][] testData = map2.get("data");
        float[][] test = map2.get("label");
        float[] testLable = new float[test.length];
        for(int i = 0; i < test.length; ++i){
            testLable[i] = test[i][0];
        }

        //create 3 classifiers to use in OVO multi-classification
        svm svmRI = new svm(true);
        svmRI.setC(1);
        svmRI.training(trainDataRI, trainLableRI);

        svm svmRD = new svm(true);
        svmRD.setC(1);
        svmRD.training(trainDataRD, trainLableRD);

        svm svmDI = new svm(true);
        svmDI.setC(1);
        svmDI.training(trainDataDI, trainLableDI);

        int released = 0;
        int deceased = 0;
        int isolated = 0;
        int correct = 0;

        //vote phase of OVO multi-classification
        for(int i = 0; i < testLable.length; ++i){
            if(svmRI.classify(testData[i]) * testLable[i] > 0){
                ++isolated;
                if(testLable[i] == 1){ //predict state is isolated
                    ++correct;
                }
            }

            if(svmRD.classify(testData[i]) * testLable[i] > 0){
                ++deceased;
                if(testLable[i] == 2){ //predict state is deceased
                    ++correct;
                }
            }

            if(svmDI.classify(testData[i]) * testLable[i] == 0){
                ++isolated;
                if(testLable[i] == 1){ //predict state is isolated
                    ++correct;
                }
            }
        }

        //create percentage format
        NumberFormat numberFormat = NumberFormat.getInstance();
        numberFormat.setMaximumFractionDigits(5);
        String correctRate = numberFormat.format( ((float) correct / (float) testLable.length * 100));

        //printout result
        System.out.println("correct count:" + correct);
        System.out.println("accuracy:" + correctRate);

    }
}
