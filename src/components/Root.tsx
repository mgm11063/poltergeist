import {
  Box,
  Button,
  HStack,
  IconButton,
  Input,
  InputGroup,
  InputLeftElement,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  useDisclosure,
  VStack,
} from "@chakra-ui/react";
import { Link, Outlet } from "react-router-dom";
import { FaMoon, FaLock } from "react-icons/fa";
import { RiGhostFill } from 'react-icons/ri';

export default function Root() {
  const { isOpen, onClose, onOpen } = useDisclosure();
  return (
    <Box>
      <HStack
        justifyContent={"space-between"}
        py={5}
        px={10}
        borderBottomWidth={1}
      >
        <Box color="red.500">
          <Link to={"/"}>
            <RiGhostFill size={"48"} />
          </Link>
        </Box>
        <HStack spacing={2}>
          <IconButton
            variant={"ghost"}
            aria-label="Toggle dark mode"
            icon={<FaMoon />}
          />
          <Button onClick={onOpen}>Log in</Button>
          <Button colorScheme={"red"}>Sign up</Button>
        </HStack>
        <Modal onClose={onClose} isOpen={isOpen} motionPreset="scale">
          <ModalOverlay/>
          <ModalContent>
            <ModalHeader>Log in</ModalHeader>
            <ModalCloseButton />
            <ModalBody>
              <VStack>
                <InputGroup size={"md"}>
                  <InputLeftElement
                    children={
                      <Box color="gray.500">
                        <RiGhostFill/>
                      </Box>
                    }
                  />
                  <Input variant={"filled"} placeholder="Username" />
                </InputGroup>
                <InputGroup>
                  <InputLeftElement
                    children={
                      <Box color="gray.500">
                        <FaLock />
                      </Box>
                    }
                  />
                  <Input variant={"filled"} placeholder="Password" />
                </InputGroup>
              </VStack>
              <Button mt={4} colorScheme={"red"} w="100%">
                Log in
              </Button>
            </ModalBody>
          </ModalContent>
        </Modal>
      </HStack>
      <Outlet />
    </Box>
  );
}