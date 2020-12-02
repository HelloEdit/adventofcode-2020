/// Find the two entries that sum to 2020 and then multiply those two numbers together.
fn ex1(numbers: &Vec<u32>) -> () {
    for first in numbers {
        for second in numbers {
            if first + second == 2020 {
                return println!("1st: {}", first * second);
            }
        }
    }
}

/// Find the three entries that sum to 2020 and then multiply those three numbers together.
fn ex1bis(numbers: &Vec<u32>) -> () {
    for first in numbers {
        for second in numbers {
            let middle = first + second;
            if middle >= 2020 {
                continue;
            }

            for third in numbers {
                if middle + third == 2020 {
                    return println!("2nd: {}", first * second * third);
                }
            }
        }
    }
}

fn main() -> Result<(), std::io::Error> {
    use std::fs;

    let numbers: Vec<u32> = fs::read_to_string("./day01/input.txt")?
        .lines()
        .map(|item| item.parse().unwrap())
        .collect();

    ex1(&numbers);
    ex1bis(&numbers);

    Ok(())
}
