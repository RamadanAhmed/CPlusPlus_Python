#include <iostream>
#include <boost/progress.hpp>

#include <pybind11/embed.h> // everything needed for embedding

namespace py = pybind11;

int main() {
    py::scoped_interpreter guard{}; // start the interpreter and keep it alive
    py::module sys = py::module::import("pdb");
    py::module test_progress = py::module::import("test_progress");

    const unsigned long expected_count = 20;
    boost::progress_display show_progress(expected_count);
    for (int i = 0; i != expected_count; ++i) {

        ++show_progress;
    }
    return 0;
}