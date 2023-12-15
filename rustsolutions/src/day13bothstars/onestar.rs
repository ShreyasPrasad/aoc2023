use std::fs::read_to_string;

pub fn get_column_str(grid: &Vec<Vec<char>>, column: usize) -> String {
    let mut column_str: String = String::new();
    for i in 0..grid.len() {
        column_str.push(grid[i][column]);
    }
    column_str
}

pub fn get_row_str(grid: &Vec<Vec<char>>, row: usize) -> String {
    let mut row_str: String = String::new();
    for i in 0..grid[0].len() {
        row_str.push(grid[row][i]);
    }
    row_str
}

fn get_column_reflections(grid: &Vec<Vec<char>>) -> usize {
    let n = grid[0].len();

    let mut dp: Vec<Vec<bool>> = vec![vec![false; n]; n];
    let mut max_column_reflections: usize = 0;
    let mut left_columns = 0;

    for i in (0..n).rev(){
        for j in i..n {
            if i == j {
                dp[i][j] = true;
            } else if j - i == 1 {
                let first = get_column_str(grid, i);
                let second = get_column_str(grid, j);
                dp[i][j] = first == second;
            } else {
                let first = get_column_str(grid, i);
                let second = get_column_str(grid, j);
                dp[i][j] = dp[i+1][j-1] && first == second;
            }
            if (j == n-1 || i == 0) && dp[i][j] && j-i > max_column_reflections {
                max_column_reflections = j-i;
                left_columns = (j-i+1)/2 + i;
            }
        }
    }
    left_columns
}

fn get_row_reflections(grid: &Vec<Vec<char>>) -> usize {
    let m = grid.len();

    let mut dp: Vec<Vec<bool>> = vec![vec![false; m]; m];
    let mut max_row_reflections: usize = 0;
    let mut left_rows = 0;

    for i in (0..m).rev(){
        for j in i..m {
            if i == j {
                dp[i][j] = true;
            } else if j - i == 1 {
                let first = get_row_str(grid, i);
                let second = get_row_str(grid, j);
                dp[i][j] = first == second;
            } else {
                let first = get_row_str(grid, i);
                let second = get_row_str(grid, j);
                dp[i][j] = dp[i+1][j-1] && first == second;
            }
            if (j == m-1 || i == 0) && dp[i][j] && j-i > max_row_reflections {
                max_row_reflections = j-i;
                left_rows = (j-i+1)/2 + i;
            }
        }
    }
    left_rows
}


pub fn get_reflections_summary(grid: &Vec<Vec<char>>) -> usize {
    // Process veritcal reflections
    let vertical_reflections = get_column_reflections(&grid);
    
    if vertical_reflections > 0 {
        return vertical_reflections;
    }

    let horizontal_reflections = get_row_reflections(&grid);
    horizontal_reflections * 100
}

pub fn onestar_solution(){
    let mut total: u64 = 0;
    let mut grid: Vec<Vec<char>> = vec![];

    for line in read_to_string("src/day13bothstars/input").unwrap().lines() {
        if line.is_empty() {
            total += get_reflections_summary(&grid) as u64;
            grid.clear();
        } else {
            grid.push(line.chars().collect());
        }
    }

    if !grid.is_empty() {
        total += get_reflections_summary(&grid) as u64;
        grid.clear();
    }

    println!("{}", total);
}