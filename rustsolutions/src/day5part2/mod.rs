use std::time::Instant;
use std::{fs::read_to_string, vec, u64};
use std::sync::atomic::AtomicU64;
use rayon::iter::{IntoParallelIterator, ParallelIterator};

struct CategoryMapping {
    mappings: Vec<Vec<u64>>
}

impl CategoryMapping {
    fn add_mapping(&mut self, mapping_line: &str){
        let mut mapping_nums: Vec<u64> = mapping_line.split_whitespace().map(|num_str|{
            num_str.parse::<u64>().unwrap()
        }).collect();
        mapping_nums.swap(0, 1);
        self.mappings.push(mapping_nums);
    }

    fn get_mapping(&self, key: u64) -> u64 {
        for mapping in self.mappings.iter() {
            let start = mapping[0];
            let end = mapping[0] + mapping[2];
            if key >= start && key < end {
                return mapping[1] + (key - start)
            }
        }
        return key
    }
}

pub fn twostar_bruteforce() {
    let lines = read_to_string("src/day5part2/input").unwrap();
    let lines_str: Vec<&str> = lines.lines().collect();
    let seeds: Vec<&str> = lines_str[0].split(":").last().unwrap().split_whitespace().collect();
    let mut categories: Vec<CategoryMapping> = vec![];
    for _ in 0..7 {
        categories.push(CategoryMapping { mappings: vec![] })
    }

    let mut current_category = 0;
    for &line in lines_str.iter().skip(1) {
        if line.contains("soil-to-fertilizer"){
            current_category = 1;
        } else if line.contains("fertiziler-to-water"){
            current_category = 2;
        } else if line.contains("water-to-light"){
            current_category = 3;
        } else if line.contains("light-to-temperature"){
            current_category = 4
        } else if line.contains("temperature-to-humidity"){
            current_category = 5
        } else if line.contains("humidity-to-location"){
            current_category = 6
        }

        let split_line: Vec<&str> = line.split_whitespace().collect();
        if split_line.len() == 3 {
            categories[current_category].add_mapping(line);
        }
    }
    
    let atomic_min_location_number = AtomicU64::new(u64::MAX);
    seeds.chunks(2).for_each(|chunk| {
        let start_seed = chunk[0].parse::<u64>().unwrap();
        let range = chunk[1].parse::<u64>().unwrap();
        
        let now = Instant::now();
        (0..range).into_par_iter().for_each(|offset| {
            let mut value = start_seed + offset;
            for category in categories.iter() {
                value = category.get_mapping(value)
            }
            atomic_min_location_number.fetch_min(value, std::sync::atomic::Ordering::Relaxed);
        });

        println!("{} seconds for the chunk.", now.elapsed().as_secs());
    });

    let min_location_number = atomic_min_location_number.load(std::sync::atomic::Ordering::Relaxed);
    println!("{}", min_location_number);

}