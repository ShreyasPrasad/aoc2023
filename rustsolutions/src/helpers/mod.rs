use std::fmt;
use reqwest;

#[derive(Debug, Clone)]
pub struct PageInputError {
    msg: String
}

impl fmt::Display for PageInputError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let format_string = format!("Error occurred when retrieving AOC input: {}", self.msg);
        write!(f, "{}", format_string)
    }
}

impl From<reqwest::Error> for PageInputError {
    fn from(err: reqwest::Error) -> Self {
        PageInputError {
            msg: format!("Request error: {}", err)
        }
    }
}

pub fn get_page_input(day: u8) -> Result<String,  PageInputError>{
    let resp = reqwest::blocking::get(
        format!("https://adventofcode.com/2023/day/{}/input", day)
    );
    if let Ok(body) = resp {
        return body.text().map_err(Into::into)
    }
    Err(PageInputError{
        msg: format!("Request to retrieve page content for day {} did not succeed." , day)
    })
}
