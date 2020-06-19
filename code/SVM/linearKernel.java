//a linear kernel function
public class linearKernel  implements kernelFunction{
    public float compute(float []v1, float []v2){
        float sum = 0;
        for(int i = 0; i < v1.length; ++i){
            sum += v1[i] * v2[i];
        }
        return sum;
    }
}
