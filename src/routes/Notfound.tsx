import { Button, Heading, Text, VStack } from "@chakra-ui/react";
import { Link } from "react-router-dom";

export default function Notfound() {
    return (
        <VStack bg="gray.100" justifyContent={"center"} minH={"100vh"}>
            <Heading>
                Page Not Found
            </Heading>
            <Text>it seems that you're lost.</Text>
            <Link to={"/"}>
                <Button color={"red"} variant={"link"}>Go Home</Button>
            </Link>
        </VStack>
    )
}