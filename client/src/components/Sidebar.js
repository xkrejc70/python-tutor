import React, { useState } from 'react';
import { Sidebar, SubMenu, Menu, MenuItem } from 'react-pro-sidebar';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from 'AuthContext';
// icons
import { FiChevronsLeft, FiChevronsRight, FiLogIn, FiLogOut } from 'react-icons/fi';
import { FaCode, FaUpload, FaChalkboardTeacher } from 'react-icons/fa';
import { IoSettingsSharp } from "react-icons/io5";
import { MdOutlineMailOutline } from "react-icons/md";
import { TbLetterS } from "react-icons/tb";

import 'assets/global.css';

function LeftSidebar({ onCollapsedChange }) {
  const navigate = useNavigate();
  const [collapsed, setCollapsed] = useState(false);
  const [toggled, setToggled] = useState(false);

  const { isLoggedIn, logout } = useAuth();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
    onCollapsedChange(!collapsed);
  };
  const handleHomeClick = () => {
    navigate("/upload");
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };

  // TODO: move styles to .css
  return (
    <div style={{ display: "flex" }}>
      <Sidebar
        className={`app ${toggled ? "toggled" : ""}`}
        style={{ height: "100%", position: "fixed", display: "inline-block" }}
        collapsed={collapsed}
        toggled={toggled}
        handleToggleSidebar={handleToggleSidebar}
        handleCollapsedChange={handleCollapsedChange}
      >
        <main>
          <Menu>
            {collapsed ? (
              <MenuItem
                icon={<FiChevronsRight />}
                onClick={handleCollapsedChange}
              ></MenuItem>
            ) : (
              <MenuItem
                suffix={
                  <div className="icon-wrapper" onClick={handleCollapsedChange}>
                    <FiChevronsLeft />
                  </div>}
                className="menu-item"
              >
                <div className="title" onClick={handleHomeClick} >PYTHON TUTOR</div>
              </MenuItem>
            )}
            <hr />
          </Menu>

          <Menu>
            <MenuItem icon={<FaUpload />} component={<Link to="/upload" />}>Upload project</MenuItem>
            <SubMenu defaultOpen label={"Practice"} icon={<FaChalkboardTeacher />}>
              <MenuItem icon={<FaCode />} component={<Link to="/#" />}>Regex</MenuItem>
              <MenuItem icon={<TbLetterS />} component={<Link to="/proj4" />} >Scrabble</MenuItem>
              <MenuItem icon={<MdOutlineMailOutline />} component={<Link to="/proj8" />} >Email Queue</MenuItem>
            </SubMenu>
          </Menu>

            <Menu>
          <div className="menu-bottom">
              {isLoggedIn ? (
                <>
                  <MenuItem icon={<IoSettingsSharp />} component={<Link to="/settings" />}> &nbsp;&nbsp; Settings</MenuItem>
                  <MenuItem icon={<FiLogOut />} onClick={handleLogout}> &nbsp;&nbsp; Logout</MenuItem>
                </>
              ) : (
                <MenuItem icon={<FiLogIn />} component={<Link to="/login" />}>&nbsp;&nbsp; Login</MenuItem>
              )}
          </div>
            </Menu>
        </main>
      </Sidebar>
    </div>
  );
}
export default LeftSidebar;
