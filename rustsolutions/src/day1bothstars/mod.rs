use std::fs::read_to_string;
pub fn onestar_solution() {
    let mut total = 0;
    for line in read_to_string("src/day1/input").unwrap().lines() {
        let mut first_found = false;
        let mut second_found = false;
        let mut first_digit = 0; 
        let mut second_digit = 0;
        for c in line.chars() { 
            if c.is_digit(10){
                if !first_found {
                    first_found = true;
                    first_digit = c.to_digit(10).unwrap();
                } else {
                    second_found = true;
                    second_digit = c.to_digit(10).unwrap();
                }   
            }
        }
        if !second_found {
            total += first_digit * 10 + first_digit
        } else {
            total += first_digit * 10 + second_digit
        }
    }
    println!("{}", total)
}