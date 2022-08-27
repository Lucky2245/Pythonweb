#include <iosream>

using namespace std;

void say_goodbye(const char*name){
  cout << "Goodbye" << name << "!\n";
}

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(goodbye){
  def("say_goodbye", say_goodbye);
}
