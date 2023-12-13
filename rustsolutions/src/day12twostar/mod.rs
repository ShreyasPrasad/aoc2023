use std::fs::read_to_string;

fn dp_base_case(dp: &mut  Vec<Vec<u64>>, record: &String, numbers: &Vec<usize>) {
    let n = record.len();
    let m = numbers.len();
    let group_size = *numbers.last().unwrap();

    for start in (0..n).rev() {
        let end = start + group_size;
        if n-start >= group_size {
            if record[start..=start].contains(".") {
                dp[m-1][start] = dp[m-1][start+1];
            } else if !record[start..end].contains(".") && !record[end..n].contains("#"){
                if !record[start..end].contains("?"){
                    dp[m-1][start] = 1;
                } else {
                    dp[m-1][start] = 1 + dp[m-1][start+1];
                }
            } else if start < (n-1) && dp[m-1][start+1] > 0 && record[start..=start].contains("?"){
                dp[m-1][start] = dp[m-1][start+1];
            }
        }
    }
}

fn process_record(record: String, numbers: Vec<usize>) -> u64 {
    let n = record.len();
    let m = numbers.len();
    let chars: Vec<char> = record.chars().collect();

    let mut dp: Vec<Vec<u64>> = vec![vec![0; n+1]; m+1];
    dp_base_case(&mut dp, &record, &numbers);

    for i in (0..m-1).rev() {
        for (j, c) in chars.iter().enumerate().rev() {
            let group_size = numbers[i];
            let end = j + group_size;
            if *c == '.' {
                dp[i][j] = dp[i][j+1];
            } else if *c == '?' { 
                if n-j >= group_size {
                    if !record[j..end].contains(".") {
                        if (j == 0 || chars[j-1] != '#') && (end == n || chars[end] != '#'){
                            if end < n {
                                dp[i][j] = dp[i+1][end+1] + dp[i][j+1];
                            }
                        } else {
                            dp[i][j] = dp[i][j+1];
                        }
                    } else {
                        dp[i][j] = dp[i][j+1];
                    }
                }  
            } else {
                if n-j >= group_size {
                    if !record[j..end].contains(".") {
                        if (j == 0 || chars[j-1] != '#') && (end == n || chars[end] != '#'){
                            if end < n {
                                dp[i][j] = dp[i+1][end+1] + dp[i][j+1];
                            }
                        }
                    }
                }
            }
        }
    }
    println!("{:?}", dp[0]);
    dp[0][0]
}

pub fn twostar_solution() {
    // Populate the grid and find the start square.
    let mut total = 0;
    for line in read_to_string("src/day12twostar/input").unwrap().lines() {
        let record_split: Vec<&str> = line.split_whitespace().collect();
        let record: String = record_split.first().unwrap().to_string();

        let numbers_str: &str = record_split.last().unwrap();
        let numbers: Vec<usize> = numbers_str.split(",").map(|num| { num.parse::<usize>().unwrap() }).collect();

        let mut expanded_str = String::from(&record);
        let mut expanded_numbers : Vec<usize> = Vec::from(numbers.clone());
        
        /*
        for _ in 0..4{
            expanded_str += &("?".to_owned() + &record);
            expanded_numbers.extend(numbers.clone());
        }
        */

        total += process_record(expanded_str, expanded_numbers);
    }

    print!("{}", total);
}