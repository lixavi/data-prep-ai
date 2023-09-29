package hello;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @RequestMapping("/")
        public String index() {
            return "This is the index awab ahmed noveenn !\n";
        }
    @RequestMapping("/hello")
        public String index2() {

            return "Hello, World!\n";
        }

}


