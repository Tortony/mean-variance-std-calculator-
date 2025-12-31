import pandas as pd

def calculate_demographic_data():
    # ডেটা লোড করা
    df = pd.read_csv('adult.data.csv')
    
    # ১. প্রতিটি race-এর লোক সংখ্যা
    race_count = df['race'].value_counts()
    
    # ২. পুরুষদের গড় বয়স
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # ৩. Bachelor's ডিগ্রির শতাংশ
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 
        1
    )
    
    # ৪. উচ্চ শিক্ষিতদের মধ্যে >50K আয়ের শতাংশ
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[higher_education & (df['salary'] == '>50K')].shape[0] / 
         df[higher_education].shape[0]) * 100, 
        1
    )
    
    # ৫. নিম্ন শিক্ষিতদের মধ্যে >50K আয়ের শতাংশ
    lower_education = ~higher_education
    lower_education_rich = round(
        (df[lower_education & (df['salary'] == '>50K')].shape[0] / 
         df[lower_education].shape[0]) * 100, 
        1
    )
    
    # ৬. সর্বনিম্ন কাজের ঘন্টা
    min_work_hours = df['hours-per-week'].min()
    
    # ৭. সর্বনিম্ন ঘন্টা কাজ করা ধনী লোকের শতাংশ
    min_hours = df['hours-per-week'] == min_work_hours
    rich_percentage = round(
        (df[min_hours & (df['salary'] == '>50K')].shape[0] / 
         df[min_hours].shape[0]) * 100, 
        1
    )
    
    # ৮. সবচেয়ে বেশি ধনী শতাংশের দেশ
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').sum() / len(x) * 100
    )
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)
    
    # ৯. ভারতে ধনী লোকদের সবচেয়ে জনপ্রিয় পেশা
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# টেস্ট করার জন্য
if __name__ == "__main__":
    result = calculate_demographic_data()
    for key, value in result.items():
        print(f"{key}: {value}")
