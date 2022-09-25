import React from "react";
import Index from "./Index";
import styled from 'styled-components';

const Wrapper = styled.div`
    width: 90%;
    height: 100%;
    min-height: 100vh;
    margin: 0 auto;
`;

const Nav = styled.div`
    width: 100%;
    height: 80px;
    text-align: center;
    line-height: 80px;
    background-color: #318d52;
    color: #fff;
    font-weight: bold;
    font-size: 20px;
`;

const Description = styled.div`
    width: 100%;
    font-size: 15px;
    font-weight: bolder;
    text-align: center;
    margin-bottom: 80px;
`;


const PageWrapper = (props) =>{
    return(
        <React.Fragment>
            <Nav>
                Colores Favoritos
            </Nav>            
            <Description>
                Selecciona un usuario para saber su color favorito
            </Description>
            <Wrapper>
                {props.children}
            </Wrapper>
        </React.Fragment>
    )
}

const App = () =>{
    return (
        <PageWrapper>
            <Index/>
        </PageWrapper>
    );
}

export default App;