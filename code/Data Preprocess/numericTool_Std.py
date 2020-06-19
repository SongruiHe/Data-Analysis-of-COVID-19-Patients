from sklearn import preprocessing
import pandas as pd


# Use LabelEncoder to encode the categorical data
def encoder():
    df = pd.read_csv("PatientInfo-label.csv")
    label_encoder = preprocessing.LabelEncoder()

    label_encoder.fit(df['sex'])
    print(label_encoder.classes_)
    df['sex'] = label_encoder.transform(df['sex'])

    label_encoder.fit(df['disease'])
    print(label_encoder.classes_)
    df['disease'] = label_encoder.transform(df['disease'])

    label_encoder.fit(df['country'])
    print(label_encoder.classes_)
    df['country'] = label_encoder.transform(df['country'])

    label_encoder.fit(df['province'])
    print(label_encoder.classes_)
    df['province'] = label_encoder.transform(df['province'])

    label_encoder.fit(df['city'])
    print(label_encoder.classes_)
    df['city'] = label_encoder.transform(df['city'])

    label_encoder.fit(df['infection_case'])
    print(label_encoder.classes_)
    df['infection_case'] = label_encoder.transform(df['infection_case'])

    df.to_csv('afterEncoding.csv')


# Use MaxAbsScaler to standardize the data
def scale():
    df = pd.read_csv('afterEncoding.csv')
    scaler = preprocessing.MaxAbsScaler()
    temp = scaler.fit_transform(df.loc[:, ['age', 'country', 'province', 'city', 'infection_case']])
    temp = pd.DataFrame(temp)

    df['age'] = temp[0]
    df['country'] = temp[1]
    df['province'] = temp[2]
    df['city'] = temp[3]
    df['infection_case'] = temp[4]
    df.to_csv("afterEncoding_std.csv")


if __name__ == '__main__':
    encoder()
    scale()
