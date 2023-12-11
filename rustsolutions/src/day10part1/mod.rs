use std::fs::read_to_string;

struct Neighbours {
    first: Vec<usize>,
    second: Vec<usize>
}

fn get_loop_neighbors(grid: &Vec<Vec<char>>, row: usize, col: usize) -> Neighbours {
    // Check the 4 directions of the given pipe to find its neighbors.
    let rows = grid.len();
    let cols = grid[0].len();
    let mut neighbors: Vec<Vec<usize>> = vec![];
    let pipe = grid[row][col];

    if row + 1 < rows 
        && (pipe == '|' || pipe == 'F' || pipe == '7' || pipe == 'S')
        && (grid[row+1][col] == '|' || grid[row+1][col] == 'J' || grid[row+1][col] == 'L' || grid[row+1][col] == 'S') {
        neighbors.push(vec![row+1, col]);
    }
    if row > 0 
       && (pipe == '|' || pipe == 'J' || pipe == 'L' || pipe == 'S')
       && (grid[row-1][col] == '|' || grid[row-1][col] == 'F' || grid[row-1][col] == '7' || grid[row-1][col] == 'S') {
        neighbors.push(vec![row-1, col]);
    }
    if col + 1 < cols 
       && (pipe == '-' || pipe == 'F' || pipe == 'L' || pipe == 'S')
       && (grid[row][col+1] == '-' || grid[row][col+1] == 'J' || grid[row][col+1] == '7' || grid[row][col+1] == 'S') {
        neighbors.push(vec![row, col+1]);
    }
    if col > 0 
       && (pipe == '-' || pipe == 'J' || pipe == '7' || pipe == 'S')
       && (grid[row][col-1] == '-' || grid[row][col-1] == 'F' || grid[row][col-1] == 'L' || grid[row][col-1] == 'S') {
        neighbors.push(vec![row, col-1]);
    }

    Neighbours { first: neighbors.first().unwrap().to_vec(), second: neighbors.last().unwrap().to_vec() }
}

pub fn onestar_solution() {
    // Populate the grid and find the start square.
    let mut grid: Vec<Vec<char>> = vec![];
    let mut s_row: usize = 0; let mut s_col: usize = 0;
    for (i, line) in read_to_string("src/day10part1/input").unwrap().lines().enumerate() {
        let mut row: Vec<char> = vec![];
        for (j, c) in line.chars().enumerate() {
            if c == 'S' {
                s_row = i;
                s_col = j;
            }
            row.push(c)
        }
        grid.push(row)
    }
    
    // Travel the loop from the an arbitrary neighbor of the start pipe.
    let starting_pipes = get_loop_neighbors(&grid, s_row, s_col);

    let mut previous_pipe = vec![s_row, s_col];
    let mut current_pipe = starting_pipes.first;
    let mut steps = 1;

    while grid[current_pipe[0]][current_pipe[1]] != 'S' {
        let next_pipes = get_loop_neighbors(&grid, current_pipe[0], current_pipe[1]);
        if next_pipes.first[0] == previous_pipe[0] && next_pipes.first[1] == previous_pipe[1] {
            previous_pipe = current_pipe;
            current_pipe = next_pipes.second
        } else {
            previous_pipe = current_pipe;
            current_pipe = next_pipes.first
        }

        steps += 1;
    }

    println!("{}", steps/2);
    
}