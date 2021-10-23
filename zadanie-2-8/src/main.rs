use std::fs::File;
use std::io::prelude::*;
use statrs::generate;

fn main() -> std::io::Result<()> {
    let q = 9;
    let n = 10i32.pow(q);
    let sums: Vec<i32> = (0..n)
        .map(|_| {
            let x = rand::random::<f32>();
            let y = rand::random::<f32>();
            if x.powi(2) + y.powi(2) < 1.0 {1} else {0}
        })
        .scan(0, |acc, el| {
            *acc += el;
            return Some(*acc);
        })
        .collect();

    let m = 10000;
    let samples: Vec<(f64, f64)> = generate::log_spaced(m, 0.0, q as f64)
        .iter()
        .map(|x| {
            let n = x.floor();
            let sum = sums[n as usize -1];
            return (n, 4.0 * sum as f64 / n);
        })
        .collect();
        
    let mut file = File::create("data.csv")?;

    for sample in samples {
        let line = format!("{},{}\n", sample.0, sample.1);
        file.write_all(line.as_bytes())?;
    }

    file.flush()?;

    Ok(())
}
