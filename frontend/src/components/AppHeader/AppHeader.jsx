// import React from 'react';
// import {
//   Header,
//   HeaderContainer,
//   HeaderName,
//   HeaderNavigation,
//   HeaderMenuButton,
//   HeaderMenuItem,
//   HeaderGlobalBar,
//   HeaderGlobalAction,
//   SkipToContent,
//   SideNav,
//   SideNavItems,
//   HeaderSideNavItems,
//   SideNavLink,
//   Button,
// } from '@carbon/react';

// import { Switcher, Notification, UserAvatar, Menu, Close,Home,Email,Information } from '@carbon/react/icons';

// import './app-header.scss'

// const AppHeader = ({isSideNavExpanded,setNav}) => {
//   console.log(isSideNavExpanded)

//   const onClickSideNavExpand = () => {
//     setNav(!isSideNavExpanded)
//   }
//   const toggleSideNav = () => {
//     setNav(!isSideNavExpanded)
//   }

//   return (
      
//       <div className='appheader'>
//       <Header className="header">

//           <button className = 'btn' onClick={onClickSideNavExpand}>
//           {isSideNavExpanded ? <Close size = {20}/> : <Menu size = {20}/>}
//           </button>

//         <HeaderName href="/" prefix="IBM" style={{color:"white"}}>
//           watsonx
//         </HeaderName>
                
//         <HeaderGlobalBar>
//         <HeaderGlobalAction aria-label="Notifications" tooltipAlignment="center" >
//           <Notification  size={20} style = {{fill:"white"}} />
//         </HeaderGlobalAction>
//         <HeaderGlobalAction aria-label="User Avatar" tooltipAlignment="center">
//           <UserAvatar size={20} style = {{fill:"white"}} />
//         </HeaderGlobalAction>
//         <HeaderGlobalAction aria-label="App Switcher" tooltipAlignment="end">
//           <Switcher size={20} style = {{fill:"white"}} />
//         </HeaderGlobalAction>
//       </HeaderGlobalBar>
//       </Header>

//         <SideNav className='side_nav'
//           aria-label="Side navigation"
//           expanded={isSideNavExpanded}
//           isPersistent = {false}
//           isRail
//         >
//           <SideNavItems >
//             {/* <HeaderSideNavItems>
//               <HeaderMenuItem href="/repos">Repositories</HeaderMenuItem>
//             </HeaderSideNavItems> */}
//           <SideNavLink onClick={toggleSideNav} href="/" renderIcon = {Home}>
//             <span style={{color:"white"}}>Home</span>
//           </SideNavLink>
//           <SideNavLink onClick={toggleSideNav} href="/" renderIcon = {Email}>
//           <span style={{color:"white"}}>Contact</span>
//           </SideNavLink>
//           <SideNavLink onClick={toggleSideNav} href="/" renderIcon = {Information}>
//           <span style={{color:"white"}}>About</span>
//           </SideNavLink>
//           </SideNavItems>
//         </SideNav>
        
//         </div>
            
//     )};


// export default AppHeader;


import React from 'react';
import {
  Header,
  HeaderName,
  HeaderGlobalBar,
  HeaderGlobalAction,
} from '@carbon/react';

import { Notification, UserAvatar, Switcher, Close, Menu } from '@carbon/react/icons';

import './app-header.scss'

const AppHeader = ({isSideNavExpanded,setNav}) => {
  console.log(isSideNavExpanded)

  const onClickSideNavExpand = () => {
    setNav(!isSideNavExpanded)
  }

  return (
    <div className='appheader'>
      <Header className="header">
        {/* <button className = 'btn' onClick={onClickSideNavExpand}>
          {isSideNavExpanded ? <Close size = {20}/> : <Menu size = {20}/>}
        </button> */}

        <HeaderName href="/" prefix="IBM" style={{color:"white"}}>
          WatsonX
        </HeaderName>
                
        <HeaderGlobalBar>
          <HeaderGlobalAction aria-label="Notifications" tooltipAlignment="center" >
            <Notification  size={20} style = {{fill:"white"}} />
          </HeaderGlobalAction>
          <HeaderGlobalAction aria-label="User Avatar" tooltipAlignment="center">
            <UserAvatar size={20} style = {{fill:"white"}} />
          </HeaderGlobalAction>
          <HeaderGlobalAction aria-label="App Switcher" tooltipAlignment="end">
            <Switcher size={20} style = {{fill:"white"}} />
          </HeaderGlobalAction>
        </HeaderGlobalBar>
      </Header>

      {/* Commented out SideNav
      <SideNav className='side_nav'
        aria-label="Side navigation"
        expanded={isSideNavExpanded}
        isPersistent = {false}
        isRail
      >
        <SideNavItems >
          <SideNavLink onClick={toggleSideNav} href="/" renderIcon = {Home}>
            <span style={{color:"white"}}>Home</span>
          </SideNavLink>
          <SideNavLink onClick={toggleSideNav} href="/" renderIcon = {Email}>
            <span style={{color:"white"}}>Contact</span>
          </SideNavLink>
          <SideNavLink onClick={toggleSideNav} href="/" renderIcon = {Information}>
            <span style={{color:"white"}}>About</span>
          </SideNavLink>
        </SideNavItems>
      </SideNav>
      */}
    </div>
  );
};

export default AppHeader;
